from django.shortcuts import render

# Controller
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question
from .forms import QuestionForm
from django.core.paginator import Paginator

def index(request):
    page = request.GET.get('page','1') #page
    # order_by is function of sorting
    question_list = Question.objects.order_by('-create_date')   # 게시물 전체
    paginator = Paginator(question_list,10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}  # question_list는 페이징 객체(page_obj)
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)

def question_create(request):
    # 링크를 통해 페이지를 요청할 경우에는 무조건 GET방식이 사용된다.
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():   # form이 유효한지를 검사한다. 만약 form에 저장된 subject, content의 값이 올바르지 않다면 form에는 오류 메시지가 저장되고 form.is_valid()가 실패하여 다시 질문 등록 화면을 렌더링 할 것이다
            question = form.save(commit=False)  # form에 저장된 데이터로 Question 데이터를 저장하기 위한 코드, commit=False는 임시 저장을 의미
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)