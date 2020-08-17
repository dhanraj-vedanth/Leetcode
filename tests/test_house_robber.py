from house_robber_198.main import Solution


def test_house_success():
    sol = Solution()
    assert sol.rob([1, 2, 3, 1]) == 4
