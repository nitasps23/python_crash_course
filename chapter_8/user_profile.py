# Using Arbitrary Keyword Arguments

# write functions that accept as many key-value
# pairs as the calling statement provides

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    
    for key, value in user_info.items():
        profile[key] = value

    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)