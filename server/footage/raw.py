from flask import Blueprint, Response

from config.storage import raw_footage_bucket, s3_client, s3_resource

raw_footage_bp = Blueprint('raw_footage_bp', __name__)


@raw_footage_bp.route('/all', methods=['GET'])
def unedited_footage_list():
    footage_list = []
    for raw_footage in raw_footage_bucket.objects.all():
        presigned_url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': 'raw-footage',
                    'Key': raw_footage.key},
            ExpiresIn=3600)
        footage_list.append(
            {
                "key": raw_footage.key,
                "url": presigned_url
            }
        )
    return {'footage': footage_list}


@raw_footage_bp.route('/<string:key>', methods=['DELETE'])
def unedited_footage_delete(key: str):
    s3_resource.Object('raw-footage', key).delete()
    return Response(status=200)
