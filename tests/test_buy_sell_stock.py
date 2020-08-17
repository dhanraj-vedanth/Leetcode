from buy_sell_stock_121.main import Solution


def test_working_case():
    s = Solution()
    assert (s.maxProfit([7, 1, 5, 3, 6, 4]) == 5)
    assert (s.maxProfit([7, 6, 4, 3, 1]) == 0)
