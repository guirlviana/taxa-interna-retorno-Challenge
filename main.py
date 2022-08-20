from database.investment import investments
from database.installments import installments
from utils.sortCashflow import sort_financial_movement
from utils.export import export_to_json
from Entity.cashflow import Cashflow
from utils.validateFields import is_valid_fields

if __name__ == "__main__":
    
    cashflow = Cashflow()
    sort_financial_movement(investments, 'created_at')
    sort_financial_movement(installments, 'due_date')
    
    for investment in investments:
        if is_valid_fields(investment, ['amount', 'created_at']):
            cashflow.add_investment(amount=float(investment['amount']), date=investment['created_at'])

    for installment in installments:
        if is_valid_fields(installment, ['amount', 'due_date']):
            cashflow.add_installment(amount=float(installment['amount']), date=installment['due_date'])

    tir = cashflow.get_tir(by_percentage=False)
    print(tir)

    export_to_json('datas', cashflow.cashflow, tir)  