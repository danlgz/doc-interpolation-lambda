import io
import json
import base64

from docxtpl import DocxTemplate


def handler(event, context):
    body = json.loads(event['body'])
    context = body.get('context')
    if not context:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'error': 'context is required'
            })
        }

    doc = DocxTemplate('./doc/template.docx')
    doc.render(context)

    file_stream = io.BytesIO()
    doc.save(file_stream)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'document': base64.b64encode(file_stream.getvalue()).decode('utf-8', 'ignore'),
            'context': context,
        })
    }
