import  pprint
from  findit import FindIt

fi=FindIt()
fi.load_template('vip_tab',pic_path='pics/hide_keyboard.PNG')

result=fi.find(
    target_pic_name='ipad_index',
    target_pic_path='pics/music.PNG'

)

pprint.pprint(result)
