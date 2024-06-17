class simple_player():
    def __init__(self, username, x, y):
        self.username = username
        self.x = x
        self.y = y
        self.action = 1
        self.stay_on = 0
    def set_action(self, action_id):
        self.action = action_id
        
    def goto(self, x, y, furni_id ):
        self.x = x
        self.y = y
        self.stay_on = furni_id
