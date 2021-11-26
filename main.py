from nba import NBA

def download_data():
    s = NBA.get_ad_stats()
    print(s)

if __name__ == '__main__':
    # 1. download the data
    download_data()
    
    # 2. extract features
    
    # 3. train model
    
    # 4. build model
