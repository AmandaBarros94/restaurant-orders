from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append({
            'customer': customer,
            'order': order,
            'day': day
        })
        return self.orders

    def get_most_ordered_dish_per_customer(self, customer):
        customerList = []
        for i in self.orders:
            if i['customer'] == customer:
                customerList.append(i['order'])

        return max(set(customerList), key=customerList.count)

    def get_never_ordered_per_customer(self, customer):
        customer_days_list = []
        all_day_list = []

        for i in self.orders:
            all_day_list.append(i['order'])

            if i['customer'] == customer:
                customer_days_list.append(i['order'])

            all_unique_days = set(all_day_list)
        customer_unique_days = set(customer_days_list)
        return all_unique_days.difference(customer_unique_days)

    def get_days_never_visited_per_customer(self, customer):
        customer_days_list = []
        days_list = []
        for order in self.orders:
            days_list.append(order['day'])
            if order['customer'] == customer:
                customer_days_list.append(order['day'])

        unique_days_list = set(days_list)
        customer_unique_days_list = set(customer_days_list)
        return unique_days_list.difference(customer_unique_days_list)

    def get_busiest_day(self):
        all_days_list = [order["day"] for order in self.orders]
        return max(set(all_days_list), key=all_days_list.count)

    def get_least_busy_day(self):
        all_days_list = [order["day"] for order in self.orders]
        return min(set(all_days_list), key=all_days_list.count)
