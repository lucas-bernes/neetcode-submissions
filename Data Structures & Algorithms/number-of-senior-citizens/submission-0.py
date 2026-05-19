class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        passengers = []

        for data in details:
            passenger_info = {}
            passenger_info["Phone Number"] = data[0:10]
            passenger_info["Gender"] = data[10]
            passenger_info["Age"] = int(data[11:13])
            passenger_info["Seat"] = data[13:]
            passengers.append(passenger_info)
        
        seniores = [p for p in passengers if p["Age"] > 60]
        return(len(seniores))


