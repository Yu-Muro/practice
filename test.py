class ClinicData():
    """
    名前、職種、生年月日、現住所、入社年月日2009/06/15、勤続年数、グレード、セミナー受講歴
    """
    data_list = ["name", "ruby", "job", "birth", "address", "entry_data", "year", "grade", "history"]
    def __init__(self):
        self.personal_data = { k: "No Data" for k in self.data_list}
        self.personal_data["entry_data"] = []


x = ClinicData()
print(x.personal_data)