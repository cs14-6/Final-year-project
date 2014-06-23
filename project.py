import tornado
from tornado.options import define, options
import tornado.web
import tornado.httpserver
import tornado.ioloop
import os.path
from dataModelsForImageStorage import SkinImage

__SKINIMAGES__ = os.path.join(os.path.dirname(__file__), 'skinImages/')

define("port", default=9000, help="Run the application on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        return self.render('index.html', title="Home - Final Year Project", message='')

    def post(self, *args, **kwargs):
        if dict(self.request.files).__len__() == 0:
            self.render('index.html', message="No image detected. Please try again", title="Image upload error")
        else:
            skinPicture = self.request.files['skin_image'][0]
            skinPictureName = skinPicture['filename']
            skinPictureExtension = os.path.splitext(skinPictureName)[1]
            open(__SKINIMAGES__ + skinPictureName, 'w').write(skinPicture['body'])

            #Save Skin Image Information to database
            skinImage = SkinImage(patientAge=self.get_argument('patient_age'),
                                  patientLocation=self.get_argument('patient_location'),
                                  skinConditionDescription=self.get_argument('condition_description'),
                                  skinImageName=skinPictureName,
                                  skinImageExtension=skinPictureExtension)
            if skinImage.saveSkinImage():
                self.render('index.html', title="Image successfully uploaded", message="Image Upload successfully")
            else:
                self.render('index.html', title="Image information not saved",
                            message="Image information not saved because of an error")


class ViewUploadedImagesHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        imagesRetrieved = SkinImage().retrieveImages()
        self.render('viewImages.html', title='Uploaded Images', message='', images=imagesRetrieved)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/", IndexHandler),
            (r"/images", ViewUploadedImagesHandler),
            (r"/skinImages/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), "skinImages")}),
        ],
        cookie_secret="alkfa';438u98u54;aodfliahg0;.,;'oiau98kjin",
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True
    )
    tornado.httpserver.HTTPServer(app).listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
