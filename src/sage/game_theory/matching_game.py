from sage.structure.sage_object import SageObject


class MatchingGame(SageObject):
    r"""
    """
    def __init__(self, num_pairs=0):
        r"""
        """
        self.suitors = []
        self.reviewers = []
        for i in range(num_pairs):
            self.add_suitor()
            self.add_reviewer()

    def _repr_(self):
        r"""
        """
        pass

    def _latex(self):
        r"""
        """
        pass

    def _is_complete(self):
        r"""
        """
        if len(self.suitors) != len(self.reviewers):
            raise ValueError("Must have the same number of reviewers as suitors")

        for suitor in self.suitors:
            if sorted(suitor.pref) != sorted(self.reviewers):
                raise ValueError("Preferences incomplete")

        for reviewer in self.reviewers:
            if sorted(reviewer.pref) != sorted(self.suitors):
                raise ValueError("Preferences incomplete")

        return True

    def add_suitor(self, name=False):
        r"""
        """
        if name is False:
            name = len(self.suitors)
        new_suitor = _Player(name, 'suitor', len(self.reviewers))
        self.suitors.append(new_suitor)
        for r in self.reviewers:
            r.pref = [-1 for s in self.suitors]

    def add_reviewer(self, name=False):
        r"""
        """
        if name is False:
            name = len(self.reviewers)
        new_reviewer = _Player(name, 'reviewer', len(self.suitors))
        self.reviewers.append(new_reviewer)
        for s in self.suitors:
            s.pref = [-1 for r in self.reviewers]


class _Player():
    def __init__(self, name, player_type, len_pref):
        self.name = name
        self.type = player_type
        self.pref = [-1 for i in range(len_pref)]

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return repr(self.name)

