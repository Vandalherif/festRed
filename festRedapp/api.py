__author__ = 'ugur'
__coding__="utf-8"
import festRedapp.algoritma.db_config
from festRedapp.algoritma.db_config import db
from django.core.urlresolvers import reverse

from bson import ObjectId
from tastypie import fields
from tastypie.resources import Resource

class Document(dict):
    __getattr__ = dict.get


class DocumentResource(Resource):


    id = fields.CharField(attribute="_id")
    title = fields.CharField(attribute="title")
    entities = fields.ListField(attribute="entities", null=True)

    class Meta:
        resource_name = "users"
        list_allowed_methods = ["get", "post"]
        detail_allowed_methods = ["get", "put", "delete"]
        #authorization = Authorization()
        object_class = Document

    def obj_get_list(self, request=None, **kwargs):

        return map(Document, db.documents.find())

    def obj_get(self, request=None, **kwargs):

        return Document(db.documents.find_one({ "_id": ObjectId(kwargs.get("pk")) }))

    def obj_create(self, bundle, **kwargs):

        db.documents.insert(bundle.data)
        return bundle

    def obj_update(self, bundle, request=None, **kwargs):

        db.documents.update({"_id": ObjectId(kwargs.get("pk")) }, { "$set": bundle.data })
        return bundle

    def obj_delete(self, request=None, **kwargs):

        db.documents.remove({ "_id": ObjectId(kwargs.get("pk")) })

    def get_resource_uri(self, item):

        # Document objesi olarak geliyor. Bunu kontrol ettikten sonra
        # Django'nun reverse fonksiyonu ile url'imizi sorguluyoruz.
        pk = item.obj._id if isinstance(item, Bundle) else item._id
        return reverse("api_dispatch_detail", kwargs={
            "resource_name": self._meta.resource_name,
            "pk": pk
        })