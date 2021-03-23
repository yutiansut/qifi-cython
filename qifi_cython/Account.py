from .struct.Deque import Deque2D
from uuid import uuid4
import numpy as np

class Trade(Deque2D):
    def __init__(self):
        super().__init__(
            'trade_id',
            {
                'seqno': np.int,
                'user_id': np.object,
                'trade_id': np.object,
                'exchange_id': np.object,
                'instrument_id': np.object,
                'order_id': np.object,
                'exchange_trade_id': np.object,
                'direction': np.object,
                'offset': np.object,
                'volume': np.float64,
                'price': np.float64,
                'trade_date_time': np.int64,
                'commission': np.float64,
                }
            )

class Order(Deque2D):
    def __init__(self):
        super().__init__(
            'order_id', 
            {
                'seqno': np.int,
                'user_id': np.object,
                'order_id': np.object,
                'exchange_id': np.object,
                'instrument_id': np.object,
                'direction': np.object,
                'offset': np.object,
                'volume_orign': np.float64,
                'price_type': np.object,
                'limit_price': np.float64,
                'time_condition': np.object,
                'volume_condition': np.object,
                'insert_date_time': np.int64,
                'exchange_order_id': np.object,
                'status': np.object,
                'volume_left': np.float64,
                'last_msg': np.object,
                }
            )

    def send_order(self, order_id: str = ''):#, code: str, amount: float, price: float, towards: int, order_id: str = '', datetime: str = ''
        order = {
            'seqno': int(1),
            'user_id': 'user_id',
            'order_id': str(uuid4() if order_id == '' else order_id),
            'exchange_id': 'exchange_id',
            'instrument_id': 'instrument_id',
            'direction': 'direction',
            'offset': 'offset',
            'volume_orign': float(0),
            'price_type': 'price_type',
            'limit_price': float(1),
            'time_condition': 'time_condition',
            'volume_condition': 'volume_condition',
            'insert_date_time': int(1),
            'exchange_order_id': 'exchange_order_id',
            'status': 'status',
            'volume_left': float(100),
            'last_msg': 'last_msg',
            }
        self.append(order)
        return order

class Position(Deque2D):
    def __init__(self):
        super().__init__(
            'instrument_id', 
            {
                'user_id': np.object,
                'exchange_id': np.object,
                'instrument_id': np.object,
                'volume_long_today': np.float64,
                'volume_long_his': np.float64,
                'volume_long': np.float64,
                'volume_long_frozen_today': np.float64,
                'volume_long_frozen_his': np.float64,
                'volume_long_frozen': np.float64,
                'volume_short_today': np.float64,
                'volume_short_his': np.float64,
                'volume_short': np.float64,
                'volume_short_frozen_today': np.float64,
                'volume_short_frozen_his': np.float64,
                'volume_short_frozen': np.float64,
                'volume_long_yd': np.float64,
                'volume_short_yd': np.float64,
                'pos_long_his': np.float64,
                'pos_long_today': np.float64,
                'pos_short_his': np.float64,
                'pos_short_today': np.float64,
                'open_price_long': np.float64,
                'open_price_short': np.float64,
                'open_cost_long': np.float64,
                'open_cost_short': np.float64,
                'position_price_long': np.float64,
                'position_price_short': np.float64,
                'position_cost_long': np.float64,
                'position_cost_short': np.float64,
                'last_price': np.float64,
                'float_profit_long': np.float64,
                'float_profit_short': np.float64,
                'float_profit': np.float64,
                'position_profit_long': np.float64,
                'position_profit_short': np.float64,
                'position_profit': np.float64,
                'margin_long': np.float64,
                'margin_short': np.float64,
                'margin': np.float64,
                }
            )

class Bank(Deque2D):
    def __init__(self):
        super().__init__(
            'id', 
            {
                'id': np.object,
                'name': np.object,
                'bank_account': np.object,
                'fetch_amount': np.float64,
                'qry_count': np.float64,
                }
            )

class Account():
    def __init__(self):
        self.account_cookie: str = ''
        self.password: str = ''
        self.portfolio: str = ''
        self.broker_name: str = ''
        self.capital_password: str = ''
        self.bank_password: str = ''
        self.bankid: str = ''
        self.investor_name: str = ''
        self.money: float = float(0),
        self.settlement: dict = dict()
        self.taskid: str = ''
        self.trade_host: str = ''
        self.updatetime: str = ''
        self.bankname: str = ''
        self.trading_day: str = ''
        self.status: int = int(0)

        self.accounts: dict = {
            'user_id': '',
            'currency': '',
            'pre_balance': '',
            'deposit': '',
            'withdraw': '',
            'WithdrawQuota': '',
            'close_profit': '',
            'commission': '',
            'premium': '',
            'static_balance': '',
            'position_profit': '',
            'float_profit': '',
            'balance': '',
            'margin': '',
            'frozen_margin': '',
            'frozen_commission': '',
            'frozen_premium': '',
            'available': '',
            'risk_ratio': '',
            }
        self.banks: Bank = Bank()
        self.event: dict = dict()
        self.orders: Order = Order()
        self.positions: Position = Position()
        self.trades: Trade = Trade()
        self.transfers: dict = dict()

class QIFI(Account):
    def __init__(self):
        super().__init__()
        self.databaseip: str = ''
        self.pub_host: str = ''
        self.wsuri: str = ''
        self.ping_gap: int = int(0)
        self.eventmq_ip: str = ''

if __name__ == "__main__":
    acc = Account()
    acc.orders.send_order()
    order = acc.orders.send_order()
    print(acc.orders.to_pandas())

    acc.orders.update(order['order_id'], {'user_id':'update'})
    print(acc.orders.get(order['order_id']))

    print(acc.orders.to_dict())