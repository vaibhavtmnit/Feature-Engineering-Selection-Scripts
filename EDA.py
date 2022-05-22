from scipy.stats import chi2_contingency

def cat_target(feat=None, target=None, data=None, *args, **kwrgs):
    
    temp = data.copy()
    temp['val'] = 1
    
    if isinstance(feat, int):
        feat = data.columns[feat]

        
    cross_tab = pd.crosstab(index=temp[feat],columns=temp[target],values=temp['val'],aggfunc=len, margins=True
                           )
    contingency = pd.crosstab(index=temp[feat],columns=temp[target],values=temp['val'],aggfunc=len).to_numpy()
    
    cross_tab_norm = pd.crosstab(index=temp[feat],columns=temp[target],values=temp['val'],aggfunc=len, margins=True, normalize=True
                           )
    
    
    _,p,_,_ = chi2_contingency(contingency)
    
    print('------------------- \n',
          cross_tab,
         '\n------------------ \n', 
          cross_tab_norm,
         '\n------------------ \n','Probability : ',str(p))
