import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x = np.random.rand(10,4)
df = pd.DataFrame(x,columns=['a','b','c','d'])
df.plot.bar()
plt.show()


#or try this 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x = np.random.rand(10,4)
df = pd.DataFrame(x,columns=['a','b','c','d'])
df.plot(kind="bar",figsize=(10,5))
plt.show()
