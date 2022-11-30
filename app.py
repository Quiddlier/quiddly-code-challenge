from flask import Flask
from flask_restx import Api, Resource, fields


# APP

app = Flask(__name__)
api = Api(app, version='1.0', title='PaymentSystem API', description='A simple payment API')


# DAO

class InvoiceDataAccessObject(object):
    """
    We have not added a database in this example.
    The data access object (DAO) is the in-memory data store used as a placeholder.
    """
    def __init__(self):
        self._counter = 0
        self.invoices = []

    def get(self, id):
        for invoice in self.invoices:
            if invoice['id'] == id:
                return invoice
        api.abort(404, f"There is no invoice with id {id}")

    def create(self, data):
        invoice = data
        invoice['id'] = self._counter = self._counter + 1
        self.invoices.append(invoice)
        return invoice

    def update(self, id, data):
        invoice = self.get(id)
        invoice.update(data)
        return invoice


dao = InvoiceDataAccessObject()

# INVOICE

invoice_namespace = api.namespace('invoice', description='invoice operations')

invoice_model = api.model('Invoice', {
    'id': fields.Integer(readonly=True, description='The invoice unique identifier'),
    'sender': fields.String(required=True, description='The sender of the invoice'),
    'receiver': fields.String(required=True, description='The receiver of the invoice'),
    'total_amount': fields.Float(required=True, description='Total invoice amount of money owed'),
    'outstanding_amount': fields.Float(required=True, description='Current invoice amount of money owed'),
    # ToDo improvement handle decimals by rounding to two decimal places for money types and add currency
    })


@invoice_namespace.route('')
class Invoices(Resource):
    @invoice_namespace.doc('List all invoices')
    @invoice_namespace.marshal_list_with(invoice_model)
    def get(self):
        """ List invoices """
        return dao.invoices

    @invoice_namespace.doc('create an invoice')
    @invoice_namespace.expect(invoice_model)
    @invoice_namespace.marshal_with(invoice_model, code=201)
    def post(self):
        """ Create new invoice """
        return dao.create(api.payload), 201


@invoice_namespace.route('/<int:id>')
@invoice_namespace.response(404, 'Invoice not found')
@invoice_namespace.param('id', 'Invoice id')
class Invoice(Resource):
    @invoice_namespace.doc('get an invoice')
    @invoice_namespace.marshal_with(invoice_model)
    def get(self, id):
        """ Fetch an invoice """
        return dao.get(id)

    @invoice_namespace.expect(invoice_model)
    @invoice_namespace.marshal_with(invoice_model)
    def put(self, id):
        """ Update an invoice """
        return dao.update(id, api.payload)


# PAYMENTS

payment_namespace = api.namespace('payment', description='payment operations')

payment = api.model('Payment', {
    'id': fields.Integer(readonly=True, description='The payment unique identifier'),
    'amount': fields.Float(required=True, description='Amount of money'),
})


@invoice_namespace.route('')
class Payments(Resource):
    ...


if __name__ == '__main__':
    app.run(debug=True)
