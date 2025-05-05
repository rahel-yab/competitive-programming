# Problem: Seat Reservation Manager - https://leetcode.com/problems/seat-reservation-manager/description/

class SeatManager:

    def __init__(self, n: int):
        self.seats = [i for i in range(1,n+1)]
        self.reserved = set()

    def reserve(self) -> int:
        seat = heappop(self.seats)
        self.reserved.add(seat)
        return seat

        

    def unreserve(self, seatNumber: int) -> None:
        if seatNumber in self.reserved:
            self.reserved.remove(seatNumber)
            heappush(self.seats,seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)