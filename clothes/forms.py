from django import forms

collection=(('1','DRESS'),('2','SKIRT'),('3','pants'))
CHEST=(('1','80'),('2','90'),('3','100'),('4','107'))
WAIST=(('1','67'),('2','87'),('3','92'),('4','97'))
HIPS =(('1','92'),('2','100'),('3','104'),('4','108'))

collections=(('1','SHIRT_SHORT'),('2','SHIRT_LONG'),('3','PANTS'))
CHEST_M=(('1','99'),('2','108'),('3','109'),('4','114'))
WAIST_M=(('1','85'),('2','90'),('3','95'),('4','100'))
HIPS_M=(('1','95'),('2','100'),('3','105'),('4','110'))


collectionn=(('1','DRESS'),('2','SKIRT'),('3','pants'))
CHEST=(('1','86'),('2','92'),('3','97'),('4','102'))
WAIST=(('1','69'),('2','74'),('3','78'),('4','84'))
HIPS =(('1','92'),('2','97'),('3','102'),('4','107'))

collectionss=(('1','SHIRT_SHORT'),('2','SHIRT_LONG'),('3','PANTS'))
CHEST_M=(('1','92'),('2','100'),('3','107'),('4','117'))
WAIST_M=(('1','79'),('2','87'),('3','94'),('4','105'))
HIPS_M=(('1','92'),('2','92'),('3','107'),('4','115'))

class select_cloth(forms.Form):
  DRESS = forms.ChoiceField(choices=collection)
  CHEST=forms.ChoiceField(choices=CHEST)
  WAIST=forms.ChoiceField(choices=WAIST)
  HIPS=forms.ChoiceField(choices=HIPS)

class male_selection(forms.Form):
  SHIRT_SHORT= forms.ChoiceField(choices=collections)
  CHEST_M=forms.ChoiceField(choices=CHEST_M)
  WAIST_M=forms.ChoiceField(choices=WAIST_M)
  HIPS_M=forms.ChoiceField(choices=HIPS_M)

class select_clotha(forms.Form):
  DRESS = forms.ChoiceField(choices=collectionn)
  CHEST=forms.ChoiceField(choices=CHEST)
  WAIST=forms.ChoiceField(choices=WAIST)
  HIPS=forms.ChoiceField(choices=HIPS)
  
class male_selectionn(forms.Form):
  SHIRT_SHORT= forms.ChoiceField(choices=collectionss)
  CHEST_M=forms.ChoiceField(choices=CHEST_M)
  WAIST_M=forms.ChoiceField(choices=WAIST_M)
  HIPS_M=forms.ChoiceField(choices=HIPS_M)