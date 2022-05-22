from sklearn.feature_selection import SelectorMixin, SelectKBest, SelectFromModel, mutual_info_regression
from sklearn.preprocessing import LabelBinarizer, LabelEncoder, Normalizer, OneHotEncoder, OrdinalEncoder
from collections import defaultdict

def get_col_info(array):
    
    array = array.to_numpy()    
    
    if array.dtype.kind in 'uU':        
        type_ ='Str'       
    elif array.dtype.kind in 'iIfF':       
        type_ = 'Numeric'
        
    len_ = len(array)

    return [len(pd.unique(array)),len(pd.unique(array))/len_,len_, type_]


# Automated Feature Importance
class AutoImportanceBivariate():
    
    def __init__(self, df, target=None):
        
        self.df = df
        self.target = target
        self._infer_dtype()
        self._str_to_num()
        
        self.importance = defaultdict(list)
    
    if self.col_type[self.target].endswith('cat'):
        
        self.mode = 'Categorical'
        
    else:
        
        self.mode = 'Continous'
        
        
        
        
    def _infer_dtype(self):
        
        # Rules for selection
        # if less than 8 or ratio less than 7.5%
        # if less than 40% then discrete
        
        col_info = self.df.apply(get_col_info, axis=0).T      
        col_info['freq_tag'] = np.where(col_info[0] <= 8 or col_info[1] < .075, 'cat',
                                       np.where(col_info[1] < .4, 'disc', 'cont'))       
        col_info['final_tag'] = col_info[3].str[:3] + col_info['freq_tag'] 
        
        cont_cols = col_info[col_info['freq_tag']!='cat'].index.to_list()
        cat_cols = ol_info[col_info['freq_tag']=='cat'].index.to_list()
        self.col_type = col_info['final_tag'].to_dict()
        
    def _str_to_num(self):
        
        str_cat_cols = [col for col,type_ in self.col_type.items() if type_.startswith('Str')]
        
        oe = OrdinalEncoder()
        self.df[str_cat_cols] = oe.fit_transform(self.df[str_cat_cols])
        
        
    
    def generate_results(self):
        
        
        
    
        

        
        
    # TODO : Implement encoding from https://stats.oarc.ucla.edu/r/library/r-library-contrast-coding-systems-for-categorical-variables/#backward
        
        
        
        
        
        
