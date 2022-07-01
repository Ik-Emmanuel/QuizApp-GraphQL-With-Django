from unicodedata import category
import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from pkg_resources import require
from .models import Quizzes, Category, Question, Answer


# ----------------------------------------
# Create object types to be used for Query
# ----------------------------------------
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")


class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id", "title", "category")


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("id", "title", "quiz", "difficulty")


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("id", "question", "answer_text", "is_right")


class Query(graphene.ObjectType):
    all_categories = DjangoListField(CategoryType)
    all_quizzes = DjangoListField(QuizzesType)
    all_questions = DjangoListField(QuestionType)
    all_answers = DjangoListField(AnswerType)
    specific_question = graphene.Field(QuestionType, id=graphene.Int())
    specific_answers = graphene.List(AnswerType, id=graphene.Int())

    def resolve_specific_question(root, info, id):
        return Question.objects.get(pk=id)

    def resolve_specific_answers(root, info, id):
        return Answer.objects.filter(question=id)



# ----------------------------------------
# Create mutation types to be used for data mutation
# ----------------------------------------
class CategoryMutation(graphene.Mutation):
    category = graphene.Field(CategoryType)
    class Arguments:
        name = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, name):
        category = Category(name=name)
        category.save()
        return CategoryMutation(category=category)


class CategoryUpdate(graphene.Mutation):
    category = graphene.Field(CategoryType)

    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, name, id):
        category = Category.objects.get(id=id)
        category.name = name
        category.save()
        return CategoryMutation(category=category)


class CategoryDelete(graphene.Mutation):
    category = graphene.String()
    class Arguments:
        id = graphene.ID(required=True)

    @classmethod
    def mutate(cls, root, info, id):
        category = Category.objects.get(id=id)
        category.delete()
        return f"Category with ID:{id}, has been deleted"


class QuizzesMutation(graphene.Mutation):
    # category_id = graphene.Int(required=True) 
    class Arguments:
        title = graphene.String(required=True)
        category_name = graphene.String(required=True)

    quiz = graphene.Field(QuizzesType)

    def mutate(root, info, category_name, title):
        category = Category.objects.get(name__icontains=category_name)
        quiz = Quizzes.objects.create(title=title, category=category)
        return QuizzesMutation(quiz=quiz)


class Mutation(graphene.ObjectType):
    create_category = CategoryMutation.Field()
    update_category = CategoryUpdate.Field()
    delete_category = CategoryDelete.Field()
    create_quizzes = QuizzesMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)


# ================================ Query ===============================
 # query {allQuestions{ quiz {id} title difficulty } }

# query {allCategories{id name}}

# query { allQuizzes{id title } }

# query {
#   allAnswers{
#     question{ quiz{id}  title}
#     answerText
#     isRight
#   }
# }

# query {specificQuestion(id:2){ id title difficulty}}


# query { specificAnswers(id:2){  question {title} answerText isRight}}


# ======================= Mutations ====================

# mutation {
#    createCategory(name:"Test" ){
#     category{
#       name
#     }
#   }
# }


# mutation{
#    createQuizzes (title:"Blockchain", categoryName:"Technology" ){
#     quiz{title category{ id name }  }
#   }
# }

# mutation{
#   updateCategory(id: 2, name: "Arts & Music"){
#     category{
#       name
#     }
#   }
# }


# mutation {
#   deleteCategory(id:6) {
#     category
#   }
# }
