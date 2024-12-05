from matchers import And, All, PlaysIn, HasAtLeast, HasFewerThan

class QueryBuilder:
    def __init__(self, matcher=All()):
        self.query_olio = matcher

    def build(self):
        return self.query_olio
    
    def plays_in(self, joukkue):
        if self.query_olio != All():
            return QueryBuilder(And(self.query_olio, PlaysIn(joukkue)))

        return QueryBuilder(PlaysIn(joukkue))
    
    def has_at_least(self, value, attribute):
        if self.query_olio != All():
            return QueryBuilder(And(self.query_olio, HasAtLeast(value, attribute)))
        return QueryBuilder(HasAtLeast(value, attribute))
    
    def has_fewer_than(self, value, attribute):
        if self.query_olio != All():
            return QueryBuilder(And(self.query_olio, HasFewerThan(value, attribute)))
        return QueryBuilder(HasFewerThan(value, attribute))