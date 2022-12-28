import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 超入門')

st.write('DateFrame')

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)
# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0), width=200, height=300)
# st.table(df.style)


#"""
# 章
## 節
### 項

#```python
#import streamlit as st
#import numpy as np
#import pandas as pd
#```

#"""
