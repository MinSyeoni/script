from dice import *

class Configuration:
    configs = ["Category","Ones", "Twos","Threes","Fours","Fives","Sixes",
                "Upper Scores","Upper Bonus(35)","Three of a kind", "Four of a kind", "Full House(25)",
                "Small Straight(30)", "Large Straight(40)", "Yahtzee(50)","Chance","Lower Scores", "Total"]

    def getConfigs(): # 정적 메소드: 객체생성 없이 사용 가능
        return Configuration.configs

    def score(row, d): # 정적 메소드: 객체생성 없이 사용 가능
    #row에 따라 주사위 점수를 계산 반환. 예를 들어, row가 0이면 "Ones"가 채점되어야 함을
    # 의미합니다. row가 2이면, "Threes"가 득점되어야 함을 의미합니다. row가 득점 (scored)하지
    # 않아야 하는 버튼 (즉, UpperScore, UpperBonus, LowerScore, Total 등)을 나타내는 경우
    # -1을 반환합니다.
        if (row>=0 and row<=6):
            return Configuration.scoreUpper(d,row+1)
        elif (row==8):
            pass

    def scoreUpper(d, num): # 정적 메소드: 객체생성 없이 사용 가능
    #Upper Section 구성 (Ones, Twos, Threes, ...)에 대해 주사위 점수를 매 깁니다. 예를 들어,
    # num이 1이면 "Ones"구성의 주사위 점수를 반환합니다.
        pass
    def scoreThreeOfAKind(d):
        pass
    def scoreFourOfAKind(d):
        pass
    def scoreFullHouse(d):
        pass
    def scoreSmallStraight(d):
    #1 2 3 4 혹은 2 3 4 5 혹은 3 4 5 6 검사
    #1 2 2 3 4, 1 2 3 4 6, 1 3 4 5 6, 2 3 4 4 5
        pass
    def scoreLargeStraight(d):
    # 1 2 3 4 5 혹은 2 3 4 5 6 검사
        pass
    def scoreYahtzee(d):
        pass
    def sumDie(d):
        pass