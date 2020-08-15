from models.Professor import Professors

class ProfessorService:
    @staticmethod
    def postProfessorOnMeetUp(professor):
        professorInserted = Professors.insert_one(professor)
        return professorInserted.inserted_id
    @staticmethod
    def updateEvent(id,professorRequest):
        Professors.update_one({'_id': id}, {'$set': professorRequest}, upsert=False)
