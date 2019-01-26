from mail_app.mail import Mail


class MockMails:

    BODY_1 = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the " \
             "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type " \
             "and scrambled it to make a type specimen book. It has survived not only five centuries, but also the " \
             "leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s " \
             "with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop " \
             "publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    PATH_MOCK_DATA = "mail_app/mail_processors/mock_data/attachment/"

    def __init__(self):
        self.mails =[]
        self.mails.append(Mail("test1@test.com", "user1@gmail.com", "Test subject 1", self.BODY_1,
                               [self.PATH_MOCK_DATA + "tomato.jpeg"], "1548515339"))
        self.mails.append(Mail("test2@test.com", "user2@gmail.com", "Test subject 2", self.BODY_1,
                               [self.PATH_MOCK_DATA + "plane_ticket.jpg", self.PATH_MOCK_DATA + "peach.png"], "1548515339"))
        self.mails.append(Mail("test3@test.com", "user3@gmail.com", "Test subject 3", self.BODY_1,
                               [], "1548515339"))


