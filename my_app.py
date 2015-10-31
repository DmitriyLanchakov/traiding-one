import main

class app(object):
	def application(env, start_response):
		ts = main.traiding_system()
		ts.main.init()
		ts.test_order("Buy")
		start_response('200 OK', [('Content-Type','text/html')])
		return [b"Hello World"]