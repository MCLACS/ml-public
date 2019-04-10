import pandas as pd
from IPython.display import display

# what if I have an integer feature that encodes categorical data
# and I want to "one hot dummy" it?

# create the DataFrame...
print("Before...")
demo_df = pd.DataFrame({'Integer Feature':[0,1,2,1],'Categorical Feature':['socks','fox','socks','box']})
display(demo_df)

# convert integer feature to string...
print("After...")
demo_df['Integer Feature'] = demo_df['Integer Feature'].astype(str)

# then one hot dummy it...
dummy = pd.get_dummies(demo_df,columns=['Integer Feature','Categorical Feature'])
pd.set_option('display.max_columns', 6)
display(dummy)


