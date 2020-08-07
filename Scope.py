

    # Add your code here
    def computeDifference(self):
        n = len(self.__elements)
        self.maximumDifference = 0
        for i in range(n):
            for j in range(1,n-i):
                self.maximumDifference = max(self.maximumDifference, abs(self.__elements[i]- self.__elements[i+j]))


