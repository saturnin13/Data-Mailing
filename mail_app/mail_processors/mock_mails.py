from mail_app.mail import Mail
from mail_app.mail_processors.ticket_processor import TicketProcessor


class MockMails:

    BODY_1 = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the " \
             "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type " \
             "and scrambled it to make a type specimen book. It has survived not only five centuries, but also the " \
             "leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s " \
             "with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop " \
             "publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    PATH_MOCK_DATA = "mail_app/mail_processors/mock_data/attachment/"

    SCRIPT = """
        <script type="application/ld+json">
        {
            "@context": "http://schema.org",
            "@type": "EventReservation",
            "reservationNumber": "881244721",
            "reservationStatus": "http://schema.org/Confirmed",
            "modifyReservationUrl": "https://www.eventbrite.com/mytickets/881244721?utm_campaign=order_confirm&amp;utm_medium=email&amp;ref=eemailordconf&amp;utm_source=eb_email&amp;utm_term=googlenow",
            "underName": {
                "@type": "Person",
                "name": "Sixte de Maupeou d&#39;Ableiges"
            },
            "reservationFor": {
                "@type": "Event",
                "name": "IC Hack 19",
                    "startDate": "2019-01-26T10:00:00+00:00",
                    "endDate": "2019-01-27T17:00:00+00:00",
                    "location": {
                        "@type": "Place",
                        "name": "Imperial College London",
                        "address": {
                            "@type": "PostalAddress",
                            "streetAddress": "Business School (Main) EntranceExhibiton RoadSW7 2AZ London",
                            "addressLocality": "London",
                            "addressRegion": "Greater London",
                            "postalCode": "SW7 2AZ",
                            "addressCountry": "GB"
                        }
                    }
            }
        }
    </script>
    """

    def __init__(self):
        self.mails =[]
        self.mails.append(Mail("orders@eventbrite.com", "user1@gmail.com", "Your Tickets for Buttoned Down Disco",
                               self.SCRIPT, [self.PATH_MOCK_DATA + "tomato.jpeg"], "1548515339"))
        self.mails.append(Mail("test1@test.com", "user1@gmail.com", "Test subject 1", self.BODY_1,
                               [self.PATH_MOCK_DATA + "tomato.jpeg"], "1548515339"))
        self.mails.append(Mail("test2@test.com", "user2@gmail.com", "Test subject 2", self.BODY_1,
                               [self.PATH_MOCK_DATA + "plane_ticket.jpg", self.PATH_MOCK_DATA + "peach.png"], "1548515339"))
        self.mails.append(Mail("test3@test.com", "user3@gmail.com", "Test subject 3", self.BODY_1,
                               [], "1548515339"))
mockmails = MockMails()
ticket_processor = TicketProcessor()
for mail in mockmails.mails:
    ticket_processor.process(mail)