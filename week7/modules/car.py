class car():
    def __init__(self, url, price, km):
        self.url = url
        self.price = price.replace(".", "")
        self.km = km.replace(".", "")
        self.price_pr_km = int(
            self.price)/int(self.km) if self.price != "Ring" else "Ring" 
    @staticmethod
    def cheapest_pr_km(car_list):
        filtered_cars = filter(lambda x: x.price_pr_km != "Ring", car_list)
        sorted_cars = sorted(filtered_cars, key=lambda x: x.price_pr_km)
        return sorted_cars[0]