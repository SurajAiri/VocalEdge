
class Activity:
    def __init__(self, title, description, questionCount, promptTopic, prepareTime):
        self.title = title
        self.description = description
        self.questionCount = questionCount
        self.promptTopic = promptTopic
        self.prepareTime = prepareTime

    def __init__(self,json):
        self.title = json['title']
        self.description = json['description']
        self.questionCount = json['questionCount']
        self.promptTopic = json['promptTopic']
        self.prepareTime = json['prepareTime']

    def toJson(self):
        return {
            'title': self.title,
            'description': self.description,
            'questionCount': self.questionCount,
            'promptTopic': self.promptTopic,
            'prepareTime': self.prepareTime
        }
