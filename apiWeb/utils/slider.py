from apiWeb.models.slider import Slider


class UtilSlider:
    @staticmethod
    def get_slider(slider: Slider):
        try:
            slider_obj = {"id": int(slider.id),
                          "image": str(slider.image_link),
                          "link": str(slider.link),
                          "type": str(slider.get_type_display())}
            return slider_obj
        except Exception as e:
            print("Error slider :", str(e))
            return str(e)

    @staticmethod
    def get_latest_slider():
        try:
            latest_slider = Slider.objects.order_by('-id')[:6]
            result_slider = map(lambda slider: UtilSlider.get_slider(slider), latest_slider) if latest_slider else []
            return result_slider

        except Exception as e:
            return [str(e)]

    @staticmethod
    def get_all_slider():
        try:
            all_slider = Slider.objects.order_by('-id')
            result_slider = map(lambda slider: UtilSlider.get_slider(slider), all_slider) if all_slider else []
            return result_slider

        except Exception as e:
            return [str(e)]
