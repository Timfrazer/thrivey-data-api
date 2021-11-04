from faker import Faker
from faker.providers import internet

# Init faker with providers
fake = Faker()
fake.add_provider(internet)

# Generate IPV4 column for Pandas DF
def add_fake_ipv4_col(pandas_df):
    for index,row in pandas_df.iterrows():
        pandas_df.loc[index,'ipv4'] = fake.ipv4_private()
    return pandas_df

