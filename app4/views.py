from django.shortcuts import render, redirect
from django.utils import timezone
from django.utils.datetime_safe import datetime
from django.views import View
from app2.models import VisitToTT, UserProfile, TextSlide
from .forms import VisitToTTForm, TextSlideForm
from django.shortcuts import get_object_or_404
import json
from django.http import JsonResponse


class VisitToTTView(View):
    template_name = 'app4/index.html'
    template_rbm_search = 'app4/rbm_search.html'


    def get(self, request, *args, **kwargs):
        user_profile = request.user.userprofile
        if user_profile.role == 'rbm':
            rbm_user_profile = UserProfile.objects.get(user=request.user)
            rbm_subordinates = UserProfile.objects.filter(rbm=rbm_user_profile)
            visits = VisitToTT.objects.filter(user_profile__in=rbm_subordinates)
            print(visits)
            return render(request, self.template_rbm_search, {'visits': visits})
        else:
            visits = VisitToTT.objects.filter(user_profile=user_profile)

            return render(request, self.template_name, {'visits': visits})




class EditVisitToTTView(View):
    template_name = 'app4/edit_visit_to_tt.html'
    template_rbm_total = 'app4/rbm_total.html'


    def get(self, request, pk, *args, **kwargs):
        user_profile = request.user.userprofile
        if user_profile.role == 'rbm':
            reports_users = VisitToTT.objects.filter(pk=pk).values(
                                                                'user_profile__user__username',
                                                                'user_profile__user__first_name',
                                                                'user_profile__photo',
                                                                'user_profile__workplace',
                                                                'visits',
                                                                'retail',
                                                                'sto',
                                                                'retail_buy_SAKURA_and_have',
                                                                'sto_buy_SAKURA_and_have',
                                                                'sto_dont_buy_SAKURA_and_have',
                                                                'retail_dont_buy_SAKURA_and_have',
                                                                'month',
                                                                'id'
            )

            text_sliders_dict = []

            for i in reports_users:
                text_sliders = TextSlide.objects.filter(visit_id=i['id']).values('title', 'text', 'text_image')
                text_sliders_dict.append({'id': i['id'], 'text_sliders': text_sliders})

            context = {
                'reports_users': reports_users,
                'text_sliders_dict': text_sliders_dict,
            }
            return render(request, self.template_rbm_total, context=context)

        else:
            visit = get_object_or_404(VisitToTT, pk=pk)
            form = VisitToTTForm(instance=visit)
            text_slides = TextSlide.objects.filter(visit=visit)
            text_slide_forms = [TextSlideForm(instance=text_slide) for text_slide in text_slides]

            return render(request, self.template_name, {'form': form, 'visit': visit, 'text_slide_forms': text_slide_forms})

    def post(self, request, pk, *args, **kwargs):
        post_data = request.POST.copy()
        incoming_date_str = post_data['month'] + '-01'

        retail = post_data['retail']
        sto = post_data['sto']
        retail_buy_SAKURA_and_have = post_data['retail_buy_SAKURA_and_have']
        sto_buy_SAKURA_and_have = post_data['sto_buy_SAKURA_and_have']
        sto_dont_buy_SAKURA_and_have = post_data['sto_dont_buy_SAKURA_and_have']
        retail_dont_buy_SAKURA_and_have = post_data['retail_dont_buy_SAKURA_and_have']
        incoming_date = datetime.strptime(incoming_date_str, '%Y-%m-%d')
        month = incoming_date.strftime('%Y-%m-%d')

        VisitToTT.objects.filter(pk=pk).update(
            retail=retail,
            sto=sto,
            retail_buy_SAKURA_and_have=retail_buy_SAKURA_and_have,
            sto_buy_SAKURA_and_have=sto_buy_SAKURA_and_have,
            sto_dont_buy_SAKURA_and_have=sto_dont_buy_SAKURA_and_have,
            retail_dont_buy_SAKURA_and_have=retail_dont_buy_SAKURA_and_have,
            month=month,
            user_profile=request.user.userprofile
        )
        return redirect('visit-to-tt-list')



class EditSlide(View):
    def post(self, request, slide_id, *args, **kwargs):
        text_slide = get_object_or_404(TextSlide, id=slide_id)
        text_slide_form = TextSlideForm(request.POST, request.FILES, instance=text_slide)

        if text_slide_form.is_valid() and text_slide_form.is_valid():
            text_slide_form.save()
            return redirect('visit-to-tt-list')
        else:
            # return render(request, self.template_name, {'form': form, 'visit': visit, 'text_slide_forms': [text_slide_form]})
            print("Error")


class NewSlide(View):
    def post(self, request, *args, **kwargs):
        visit_id = request.POST.get('visit')
        visit = get_object_or_404(VisitToTT, id=visit_id)
        user_profile = visit.user_profile
        text_slide_form = TextSlideForm(request.POST, request.FILES)

        if text_slide_form.is_valid():
            slide_form = text_slide_form.save(commit=False)

            # Assign the user_profile instance to the user_profile field
            slide_form.user_profile = user_profile
            slide_form.visit = visit
            slide_form.save()

            return redirect('visit-to-tt-list')
        else:
            print("Error")


class DeleteSlide(View):
    template_name = 'app4/success.html'

    def get(self, request, pk, slide_id, *args, **kwargs):
        success_delete = TextSlide.objects.filter(pk=slide_id).delete()
        if success_delete:
            return render(request, self.template_name, {'pk': pk})


class AddedRept(View):
    template_name = 'app4/added_visit.html'

    def get(self, request, *args, **kwargs):
        visit_form = VisitToTTForm()
        return render(request, self.template_name, {'form': visit_form})

    def post(self, request, *args, **kwargs):
        post_data = request.POST.copy()
        incoming_date_str = post_data['month'] + '-01'

        retail = post_data['retail']
        sto = post_data['sto']
        retail_buy_SAKURA_and_have = post_data['retail_buy_SAKURA_and_have']
        sto_buy_SAKURA_and_have = post_data['sto_buy_SAKURA_and_have']
        sto_dont_buy_SAKURA_and_have = post_data['sto_dont_buy_SAKURA_and_have']
        retail_dont_buy_SAKURA_and_have = post_data['retail_dont_buy_SAKURA_and_have']
        incoming_date = datetime.strptime(incoming_date_str, '%Y-%m-%d')
        month = incoming_date.strftime('%Y-%m-%d')

        VisitToTT.objects.create(
            retail=retail,
            sto=sto,
            retail_buy_SAKURA_and_have=retail_buy_SAKURA_and_have,
            sto_buy_SAKURA_and_have=sto_buy_SAKURA_and_have,
            sto_dont_buy_SAKURA_and_have=sto_dont_buy_SAKURA_and_have,
            retail_dont_buy_SAKURA_and_have=retail_dont_buy_SAKURA_and_have,
            month=month,
            user_profile=request.user.userprofile
        )
        return redirect('visit-to-tt-list')




class ViewRept(View):
    template_total = 'app4/rbm_total.html'

    def get(self, request, pk, *args, **kwargs):
        user_profile = request.user.userprofile
        reports_users = VisitToTT.objects.filter(pk=pk).values(
            'user_profile__user__username',
            'user_profile__user__first_name',
            'user_profile__photo',
            'user_profile__workplace',
            'visits',
            'retail',
            'sto',
            'retail_buy_SAKURA_and_have',
            'sto_buy_SAKURA_and_have',
            'sto_dont_buy_SAKURA_and_have',
            'retail_dont_buy_SAKURA_and_have',
            'month',
            'id'
        )

        text_sliders_dict = []

        for i in reports_users:
            text_sliders = TextSlide.objects.filter(visit_id=i['id']).values('title', 'text', 'text_image')
            text_sliders_dict.append({'id': i['id'], 'text_sliders': text_sliders})

        context = {
            'reports_users': reports_users,
            'text_sliders_dict': text_sliders_dict,
        }
        return render(request, self.template_total, context=context)

