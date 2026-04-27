class simpleMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        print("befor view")

        response = self.get_response(request)

        print("after view")

        return response

