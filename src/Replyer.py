class Replyer:
    def __init__(self, replyer_id: int, company: str, bonus: int, skills = []):
        self.id = replyer_id
        self.company = company
        self.bonus = bonus
        self.skills = skills
        self.dev_friends = set()
        self.po_friends = set()
        self.x = None
        self.y = None


    def make_friendship_with_dev(self, dev_id, dev_list):
        other_dev = dev_list[dev_id]
        other_skills = set(other_dev.skills.copy())

        my_skills = set(self.skills.copy())

        common_skills = my_skills & other_skills
        unique_skills = my_skills - other_skills

        power = len(common_skills) * len(unique_skills)

        if self.company == other_dev.company:
            power =+ self.bonus * other_dev.bonus

        self.dev_friends.append((dev_id, power))
        self.dev_friends.sort()

        other_dev.dev_friends.append((self.id, power))
        other_dev.dev_friends.sort()


    def make_friendship_with_po(self, po_id, po_list):
        other_po = po_list[po_id]

        power = 0

        if self.company == other_dev.company:
            power =+ self.bonus * other_dev.bonus

        self.po_friends.append((po_id, power))
        self.po_friends.sort()

        other_po.po_friends.append((self.id, power))
        other_po.po_friends.sort()