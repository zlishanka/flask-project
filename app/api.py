from flask_restful import request, reqparse, abort, Api, Resource
import common.logger as logger

class RequestResource(Resource):
    def getName(self):
        return self.__class__.__name__

    def enterReq(self, request):
        logger.logging_info("--- REST request starts ---")
        logger.logging_info("%s  %s ..."%(request.method, request.path))
        if request.args:
            logger.logging_info("query - %s "%(request.args))
        data_json = request.get_json()
        if data_json:
            logger.logging_info("data - %s "%(data_json))
        logger.logging_info(" ")

    def exitReq(self):
        logger.logging_info("--- REST request ends ---")


class ApplicationResource(RequestResource):
    def get(self):
        self.enterReq(request)
        # handle get request 
        self.exitReq()

    def post(self):
        self.enterReq(request)
        # handle post request 
        self.exitReq() 
    
    def put(self):
        self.enterReq(request)
        # handle put request 
        self.exitReq() 
    
    def delete(self):
        self.enterReq(request)
        # handle delete request
        self.exitReq()