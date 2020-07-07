import os
import traceback
from flask import Flask
from flask import request
from flask_cors import CORS
from flask_restful import Api 

import common.logger as logger
from common.constants import APPLICATION_LOGGING, APPLICATION_ROOT_ROUTE, APPLICATION_PORT
from app.api import ApplicationResource

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(ApplicationResource, APPLICATION_ROOT_ROUTE)

if __name__ == '__main__':

    if not os.path.exists(os.path.expanduser("~") + "/logs"):
        os.mkdir(os.path.expanduser("~") + "/logs") 
    logger.logging_setup(os.path.expanduser("~") + "/logs/" + APPLICATION_LOGGING, \
                            logger.LoggingLevel.INFO)
    
    logger.logging_info("loading configuration...")
    host =  '0.0.0.0' 
    port =  APPLICATION_PORT
    # certificate and key should be configured in configuration file 
    context = ("../server.crt", "../server.key") 
    logger.logging_info(" --- Streaming Manager is started at port %s ---"%(port)) 
    
    app.run(threaded=True, debug=True, ssl_context=context, host=host, port=port)
