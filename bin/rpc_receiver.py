#!/usr/bin/env python3
"""
RPC calls to python objects via HTTP Post
Run this on the host, accepts calls from rpc_sender
See ESP32/lib implementation and sample
Usage::
    ./rpc_receiver.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from dp832a import DP832A
from dsox2024a import DSOX2024A
from dmm34461a import DMM34461A

class TestObj:
    def __init__(self):
        pass
    def print_args(self, *args, **kvargs):
        print("TestObj: args={}, kwargs={}".format(args, kvargs))
        return len(args) + len(kvargs)

class _Receiver(BaseHTTPRequestHandler):

    # list of accepted objects
    # (security feature, we don't want to open up to just anything)
    RESOURCES = { "TestObj": TestObj,
            "pwr": DP832A, "scope": DSOX2024A, "dmm": DMM34461A }
    ACTIVE_RESOURCES = {}

    def response(self, resp=None, code=200):
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(resp, ensure_ascii=False).encode('gbk'))

    # return id of named resource, create if it does not exist already
    def get_resource(self, args):
        try:
            resource_name = args.get('resource', None)
            if resource_name in self.RESOURCES:
                resource_id = "$" + resource_name
                if not resource_id in self.ACTIVE_RESOURCES:
                    # instantiate resource
                    klass = self.RESOURCES[resource_name]
                    self.ACTIVE_RESOURCES[resource_id] = klass()
                # return a handle to access object in future calls
                self.response(resource_id)
            else:
                self.response("Unknown resource: {}".format(obj), 400)
        except Exception as ex:
            print("*** Exception in get_resource:", ex)
            self.response("resource '{}'".format(resource_name), code=500)

    # dispatch method call to resource
    def call_method(self, args):
        try:
            resource_id = args['resource_id']
            if resource_id:
                resource = self.ACTIVE_RESOURCES[resource_id]
                method = getattr(resource, args['method'])
                result = method(*args['args'], **args['kwargs'])
                self.response(result)
            else:
                self.response("no such resource, {}".format(resource_id), code=400)
        except Exception as ex:
            print("*** Exception in call_method", ex)
            self.response("method '{}'".format(args['method']), code=500)

    # purge resource from dictionary of active resources
    def release_resource(self, args):
        try:
            resource_id = args['resource_id']
            self.ACTIVE_RESOURCES.pop(resource_id, None)
            self.response()
        except Exception as ex:
            print("*** Exception in release_resource:", ex)
            self.response("resource '{}'".format(resource_id), code=500)

    def do_POST(self):
        try:
            path = self.path
            content_length = int(self.headers['Content-Length'])
            data = self.rfile.read(content_length)
            data = json.loads(data.decode('utf-8'))
            # process request
            if path == '/get_resource':
                self.get_resource(data)
            elif path == '/call_method':
                self.call_method(data)
            elif path == '/release_resource':
                self.release_resource(data)
            else:
                self.response(code=400)
        except Exception as ex:
            print("*** Exception in do_post:", ex)
            self.response(code=500)

    def do_GET(self):
        # we do not handle GET, just send back an error code
        self.response(400)

def run(port=8080, server_class=HTTPServer):
    print("starting RPC server on port", port)
    server_address = ('', port)
    httpd = server_class(server_address, _Receiver)
    print('Accepting incoming requests ...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv
    port = int(argv[1]) if len(argv) > 1 else 8080
    run(port)
