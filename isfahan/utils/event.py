from isfahan.models.event import Event


class UtilEvent:
    @staticmethod
    def get_event(event: Event):
        try:
            event_obj = {"id": int(event.id),
                         "name": str(event.name),
                         "date": str(event.date),
                         "location": str(event.location)}
            return event_obj
        except Exception as e:
            print("Error event :", str(e))
            return str(e)

    @staticmethod
    def get_latest_event():
        try:
            latest_event = Event.objects.order_by('-id')[:6]
            result_event = map(lambda event: UtilEvent.get_event(event), latest_event) if latest_event else []
            return result_event

        except Exception as e:
            return [str(e)]

    @staticmethod
    def get_all_event():
        try:
            all_event = Event.objects.order_by('-id')
            result_event = map(lambda event: UtilEvent.get_event(event), all_event) if all_event else []
            return result_event

        except Exception as e:
            return [str(e)]
