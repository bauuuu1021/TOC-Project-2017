from transitions.extensions import GraphMachine

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def user_to_state1(self, update):
        text = update.message.text
        return text.lower() == '書卷獎'

    def user_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'all pass'

    def user_to_state3(self, update):
        text = update.message.text
        return text.lower() == '被21'

    def state3_to_state2(self, update):
        text = update.message.text
        return text.lower() == '沒有'

    def state3_to_state4(self, update):
        text = update.message.text
        return text.lower() == '有'

    def state4_to_state5(self, update):
        text = update.message.text
        return text.lower() == '男生'

    def state4_to_state6(self, update):
        text = update.message.text
        return text.lower() == '女生'

    def on_enter_state1(self, update):
        update.message.reply_text("哇！你好棒喔！")
        self.go_back(update)

    def on_enter_state2(self, update):
        update.message.reply_text("加油！下學期拼卷！")
        self.go_back(update)

    def on_enter_state3(self, update):
        update.message.reply_text("GG!有被21過嗎？")

    def on_enter_state4(self, update):
        update.message.reply_text("你/妳是男生還是女生呢？")

    def on_enter_state5(self, update):
        update.message.reply_text("祝 當兵愉快：）")
        self.go_back(update)

    def on_enter_state6(self, update):
        update.message.reply_text("再考一次大學吧～")
        self.go_back(update)

