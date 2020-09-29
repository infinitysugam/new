from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import pandas as pd
import numpy as np


def prediction_client(request):
    return render(request, 'prediction/ptest.html')

def predict_price(request):

    # Receive data from client
    # Numerical Input
    if (request.POST):
        
        guests_included = int(request.POST.get('guests_included'))
        review_scores_cleanliness = float(request.POST.get('review_scores_cleanliness'))
        number_of_reviews_ltm = request.POST.get('number_of_reviews_ltm')
        review_scores_rating = float(request.POST.get('review_scores_rating'))
        bedrooms = int(request.POST.get('bedrooms'))
        cleaning_fee = int(request.POST.get('cleaning_fee'))
        accommodates = int(request.POST.get('accommodates'))
        review_scores_communication = float(request.POST.get('review_scores_communication'))
        bathrooms = int(request.POST.get('bathrooms'))
        maximum_nights = int(request.POST.get('maximum_nights'))
        availability_30 = int(request.POST.get('availability_30'))
        security_deposit = int(request.POST.get('security_deposit'))
        beds = int(request.POST.get('beds'))
        extra_people = int(request.POST.get('extra_people'))
        minimum_nights = int(request.POST.get('minimum_nights'))
        
        # Categorical Input
        
        host_is_superhost_t = int(request.POST.get('host_is_superhost_t'))
        host_identity_verified_t = int(request.POST.get('host_identity_verified_t'))
        is_location_exact_t = int(request.POST.get('is_location_exact_t'))
        instant_bookable_t = int(request.POST.get('instant_bookable_t'))
        require_guest_profile_picture_t = int(request.POST.get('require_guest_profile_picture_t'))
        require_guest_phone_verification_t = int(request.POST.get('require_guest_phone_verification_t'))
        
        
        
        property_type = str(request.POST.get('property_type'))
        
        processed_property_type = ['Apartment', 'Boutique_hotel', 'Guest_Suite', 'House', 'Loft', 'Other', 
                                   'Serviced_apartment', 'Townhouse']

        for prop in processed_property_type:

            var_name_prop = f"processed_property_type_{prop}"

            if prop == property_type:
                exec("%s = %d" % (var_name_prop,1),globals())
            else:
                exec("%s = %d" % (var_name_prop,0),globals())
        
        room_type = str(request.POST.get('room_type'))
        
        processed_room_type = ['Entire_home_apt', 'Private_room', 'Shared_room']

        for room in processed_room_type:

            var_name_room = f"room_type_{room}"

            if room == room_type:
                exec("%s = %d" % (var_name_room,1),globals())
            else:
                exec("%s = %d" % (var_name_room,0),globals())


        
        
        
        calendar_updated = str(request.POST.get('calendar_updated'))
        
        processed_calendar_updated = ['1_week_ago', '2_days_ago', '2_months_ago', '2_weeks_ago', '3_days_ago', '3_weeks_ago',
                                 '4_days_ago', '4_weeks_ago', '5_days_ago', '5_weeks_ago', '6_days_ago', '6_weeks_ago',
                                 '7_weeks_ago', 'more_than_2_months_ago', 'today', 'yesterday']

        

        for calendar in processed_calendar_updated:

            var_name_calen = f"processed_calendar_updated_{calendar}"

            if calendar == calendar_updated:
                exec("%s = %d" % (var_name_calen,1),globals())
            else:
                exec("%s = %d" % (var_name_calen,0),globals())

        
        
        cancellation_policy = str(request.POST.get('cancellation_policy'))
        
        processed_cancellation_policy = ['flexible', 'moderate', 'strict']

        for cancel in processed_cancellation_policy:

            var_name_cancel = f"processed_cancellation_policy_{cancel}"

            if cancel == cancellation_policy:
                exec("%s = %d" % (var_name_cancel,1),globals())
            else:
                exec("%s = %d" % (var_name_cancel,0),globals())



        host_response_rate = str(request.POST.get('host_response_rate'))
        
        processed_host_response_rate = ['0', '100', '20', '40', '60', '80']

        for response in processed_host_response_rate:

            var_name_response = f"processed_host_response_rate_{response}"

            if response == host_response_rate:
                exec("%s = %d" % (var_name_response,1),globals())
            else:
                exec("%s = %d" % (var_name_response,0),globals())
            

            
        zipcode = str(request.POST.get('zipcode'))
        
        processed_zipcode = ['60202', '60302', '60304', '60411', '60534', '60601', '60602', '60603', '60604', '60605',
                         '60606', '60607', '60608', '60609', '60610', '60611', '60612', '60613', '60614', '60615',
                         '60616', '60617', '60618', '60619', '60620', '60621', '60622', '60623', '60624', '60625',
                         '60626', '60628', '60629', '60630', '60631', '60632', '60633', '60634', '60636', '60637',
                         '60638', '60639', '60640', '60641', '60642', '60643', '60644', '60645', '60646', '60647',
                         '60649', '60651', '60652', '60653', '60654', '60655', '60656', '60657', '60659', '60660',
                         '60661', '60699', '60707', '60804', '60827', 'Other']

        for code in processed_zipcode:

            var_name_code = f"processed_zipcode_{code}"

            if code == zipcode:
                exec("%s = %d" % (var_name_code,1),globals())
            else:
                exec("%s = %d" % (var_name_code,0),globals())

                
        X = [guests_included, review_scores_cleanliness, number_of_reviews_ltm, review_scores_rating, bedrooms, 
         cleaning_fee, accommodates, review_scores_communication, bathrooms, maximum_nights, availability_30, 
         security_deposit, beds, extra_people, minimum_nights, host_is_superhost_t, host_identity_verified_t,
         is_location_exact_t, instant_bookable_t, require_guest_profile_picture_t, require_guest_phone_verification_t,
         processed_property_type_Apartment, processed_property_type_Boutique_hotel, processed_property_type_Guest_Suite,
         processed_property_type_House, processed_property_type_Loft, processed_property_type_Other,
         processed_property_type_Serviced_apartment, processed_property_type_Townhouse, room_type_Entire_home_apt,
         room_type_Private_room, room_type_Shared_room, processed_calendar_updated_1_week_ago,
         processed_calendar_updated_2_days_ago, processed_calendar_updated_2_months_ago, processed_calendar_updated_2_weeks_ago,
         processed_calendar_updated_3_days_ago, processed_calendar_updated_3_weeks_ago, processed_calendar_updated_4_days_ago,
         processed_calendar_updated_4_weeks_ago, processed_calendar_updated_5_days_ago, processed_calendar_updated_5_weeks_ago,
         processed_calendar_updated_6_days_ago, processed_calendar_updated_6_weeks_ago, processed_calendar_updated_7_weeks_ago,
         processed_calendar_updated_more_than_2_months_ago, processed_calendar_updated_today, processed_calendar_updated_yesterday,
         processed_cancellation_policy_flexible, processed_cancellation_policy_moderate, processed_cancellation_policy_strict,
         processed_host_response_rate_0, processed_host_response_rate_100, processed_host_response_rate_20,
         processed_host_response_rate_40, processed_host_response_rate_60, processed_host_response_rate_80,
         processed_zipcode_60202, processed_zipcode_60302, processed_zipcode_60304, processed_zipcode_60411,
         processed_zipcode_60534, processed_zipcode_60601, processed_zipcode_60602, processed_zipcode_60603,
         processed_zipcode_60604, processed_zipcode_60605, processed_zipcode_60606, processed_zipcode_60607,
         processed_zipcode_60608, processed_zipcode_60609, processed_zipcode_60610, processed_zipcode_60611,
         processed_zipcode_60612, processed_zipcode_60613, processed_zipcode_60614, processed_zipcode_60615,
         processed_zipcode_60616, processed_zipcode_60617, processed_zipcode_60618, processed_zipcode_60619,
         processed_zipcode_60620, processed_zipcode_60621, processed_zipcode_60622, processed_zipcode_60623,
         processed_zipcode_60624, processed_zipcode_60625, processed_zipcode_60626, processed_zipcode_60628,
         processed_zipcode_60629, processed_zipcode_60630, processed_zipcode_60631, processed_zipcode_60632,
         processed_zipcode_60633, processed_zipcode_60634, processed_zipcode_60636, processed_zipcode_60637,
         processed_zipcode_60638, processed_zipcode_60639, processed_zipcode_60640, processed_zipcode_60641,
         processed_zipcode_60642, processed_zipcode_60643, processed_zipcode_60644, processed_zipcode_60645,
         processed_zipcode_60646, processed_zipcode_60647, processed_zipcode_60649, processed_zipcode_60651,
         processed_zipcode_60652, processed_zipcode_60653, processed_zipcode_60654, processed_zipcode_60655,
         processed_zipcode_60656, processed_zipcode_60657, processed_zipcode_60659, processed_zipcode_60660,
         processed_zipcode_60661, processed_zipcode_60699, processed_zipcode_60707, processed_zipcode_60804,
         processed_zipcode_60827, processed_zipcode_Other]

        # reshape input data into 2D array

        X2 = np.array(X).reshape(1,123)

        # list the original names of the features used in training the model. Ideally, variable names should have been
        # defined with thse feature names

        features = ['guests_included', 'review_scores_cleanliness', 'number_of_reviews_ltm', 'review_scores_rating', 
                    'bedrooms', 'cleaning_fee', 'accommodates', 'review_scores_communication', 'bathrooms', 
                    'maximum_nights', 'availability_30', 'security_deposit', 'beds', 'extra_people', 'minimum_nights', 
                    'host_is_superhost_t', 'host_identity_verified_t', 'is_location_exact_t', 'instant_bookable_t', 
                    'require_guest_profile_picture_t', 'require_guest_phone_verification_t', 
                    'processed_property_type_Apartment', 'processed_property_type_Boutique hotel', 
                    'processed_property_type_Guest suite', 'processed_property_type_House', 
                    'processed_property_type_Loft', 'processed_property_type_Other', 'processed_property_type_Serviced apartment', 
                    'processed_property_type_Townhouse', 'room_type_Entire home/apt', 'room_type_Private room', 
                    'room_type_Shared room', 'processed_calendar_updated_1 week ago', 
                    'processed_calendar_updated_2 days ago', 'processed_calendar_updated_2 months ago', 
                    'processed_calendar_updated_2 weeks ago', 'processed_calendar_updated_3 days ago', 
                    'processed_calendar_updated_3 weeks ago', 'processed_calendar_updated_4 days ago', 
                    'processed_calendar_updated_4 weeks ago', 'processed_calendar_updated_5 days ago', 
                    'processed_calendar_updated_5 weeks ago', 'processed_calendar_updated_6 days ago', 
                    'processed_calendar_updated_6 weeks ago', 'processed_calendar_updated_7 weeks ago', 
                    'processed_calendar_updated_more than 2 months ago', 'processed_calendar_updated_today', 
                    'processed_calendar_updated_yesterday', 'processed_cancellation_policy_flexible', 
                    'processed_cancellation_policy_moderate', 'processed_cancellation_policy_strict', 
                    'processed_host_response_rate_0%', 'processed_host_response_rate_100%', 
                    'processed_host_response_rate_20%', 'processed_host_response_rate_40%', 
                    'processed_host_response_rate_60%', 'processed_host_response_rate_80%', 
                    'processed_zipcode_60202', 'processed_zipcode_60302', 'processed_zipcode_60304', 
                    'processed_zipcode_60411', 'processed_zipcode_60534', 'processed_zipcode_60601', 
                    'processed_zipcode_60602', 'processed_zipcode_60603', 'processed_zipcode_60604', 
                    'processed_zipcode_60605', 'processed_zipcode_60606', 'processed_zipcode_60607', 
                    'processed_zipcode_60608', 'processed_zipcode_60609', 'processed_zipcode_60610', 
                    'processed_zipcode_60611', 'processed_zipcode_60612', 'processed_zipcode_60613', 
                    'processed_zipcode_60614', 'processed_zipcode_60615', 'processed_zipcode_60616', 
                    'processed_zipcode_60617', 'processed_zipcode_60618', 'processed_zipcode_60619', 
                    'processed_zipcode_60620', 'processed_zipcode_60621', 'processed_zipcode_60622', 
                    'processed_zipcode_60623', 'processed_zipcode_60624', 'processed_zipcode_60625', 
                    'processed_zipcode_60626', 'processed_zipcode_60628', 'processed_zipcode_60629', 
                    'processed_zipcode_60630', 'processed_zipcode_60631', 'processed_zipcode_60632', 
                    'processed_zipcode_60633', 'processed_zipcode_60634', 'processed_zipcode_60636', 
                    'processed_zipcode_60637', 'processed_zipcode_60638', 'processed_zipcode_60639', 
                    'processed_zipcode_60640', 'processed_zipcode_60641', 'processed_zipcode_60642', 
                    'processed_zipcode_60643', 'processed_zipcode_60644', 'processed_zipcode_60645', 
                    'processed_zipcode_60646', 'processed_zipcode_60647', 'processed_zipcode_60649', 
                    'processed_zipcode_60651', 'processed_zipcode_60652', 'processed_zipcode_60653', 
                    'processed_zipcode_60654', 'processed_zipcode_60655', 'processed_zipcode_60656', 
                    'processed_zipcode_60657', 'processed_zipcode_60659', 'processed_zipcode_60660', 
                    'processed_zipcode_60661', 'processed_zipcode_60699', 'processed_zipcode_60707', 
                    'processed_zipcode_60804', 'processed_zipcode_60827', 'processed_zipcode_Other']

        
        # create input dataframe

        X3 = pd.DataFrame(X2, columns = features)

        # import model
        model = pd.read_pickle('prediction/xgb_01.pkl')
        
        # Predict price 
        price = np.exp(model.predict(X3))  
    

                                                                            

    context={'price':price}

    return render(request,'prediction/predict.html',context)