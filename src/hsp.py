class HarvestSchedulingProblem:
    
    class Area:
        def __init__(self, id:int) -> None:
            self.id = id
            self.size = -1
            self.adjacencies = ()
            self.profits = ()

        def __str__(self) -> str:
            return str(self.id)

    def __init__(self) -> None:
        self.n_areas = -1
        self.n_periods = -1
        self.areas = []
        self.min_natural_reserve = -1

    @staticmethod
    def make_from_input():
        hsp = HarvestSchedulingProblem()
        hsp.n_areas = int(input())
        hsp.n_periods = int(input())
        hsp.areas = [HarvestSchedulingProblem.Area(i + 1) for i in range(hsp.n_areas)]

        area_sizes = str(input()).split(' ')
        for area_id in range(len(area_sizes)):
            hsp.areas[area_id].size = int(area_sizes[area_id])

        for area in hsp.areas:
            area.adjacencies = tuple([hsp.areas[int(adjacency) - 1] for adjacency in str(input()).split(' ')])

        for _ in range(hsp.n_periods):
            period_profits = str(input()).split(' ')
            for area_id in range(len(period_profits)):
                hsp.areas[area_id].profits += (int(period_profits[area_id]),)

        hsp.min_natural_reserve = int(input())
        return hsp

    def __str__(self) -> str:
        hsp = 'Harvest Scheduling Problem\n==========================\n'
        hsp += 'No units = ' + str(self.n_areas) + '\n'
        hsp += 'No periods = ' + str(self.n_periods) + '\n'
        hsp += 'Min natural reserve size = ' + str(self.min_natural_reserve) + '\n\n'

        profits = tuple([area.profits for area in self.areas])
        profits = tuple(sum(profits, ()))

        max_id_len = len(str(max(self.areas, key = lambda area: area.id, default = 0).id))
        max_area_len = len(str(max(self.areas, key = lambda area: area.size, default = 0).size)) + 3
        max_profit_len = len(str(max(profits, default = 0))) + 3

        area_str_top = '   ||'
        area_str_bot = 'Ai ||'
        area_divider = ('=' * (5 + (max_area_len + 1) * self.n_areas)) + '\n'

        adjacencies = ''
        profit_str_top = 'Period ||'
        profit_str_others = ''
        profits_divider = ('=' * (9 + (max_profit_len + 1) * self.n_areas)) + '\n'

        for area in self.areas:
            area_str_top += ('U' + str(area.id)).center(max_area_len) + '|'
            profit_str_top += ('U' + str(area.id)).center(max_profit_len) + '|'
            area_str_bot += str(area.size).center(max_area_len) + '|'
            adjacencies += 'U' + str(area.id) + (' ' * (max_id_len - len(str(area.id)))) + ' : ' + \
                str(tuple([str(adjacency) for adjacency in area.adjacencies])) + '\n'

        hsp += 'Sizes:\n' + area_divider + area_str_top + '\n' + area_str_bot + '\n' + area_divider + '\n'
        hsp += 'Adjacencies:\n' + adjacencies + '\n'

        for period in range(self.n_periods):
            profit_str_others += '\n' + (' ' * (6 - len(str(period)))) + str(period + 1) + ' ||'
            for area in self.areas:
                profit_str_others += str(area.profits[period]).center(max_profit_len) + '|'

        hsp += 'Profits:\n' + profits_divider + profit_str_top + profit_str_others + '\n' + profits_divider
        return hsp
