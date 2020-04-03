from django.db import models


# Create your models here.
class Category(models.Model):
    names = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')

    # Ensuring that there are no category labels of the same kind
    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"
        ordering = ['names']

    def __str__(self):
        full_path = [self.names]
        k = self.parent
        while k is not None:
            full_path.append(k.names)
            k = k.parent
        return ' -> '.join(full_path[::-1])


class ProductCategory(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey('Category', null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    # def get_cat_list(self):
    #     k = self.category  # for now ignore this instance method

    #     breadcrumb = ["dummy"]
    #     while k is not None:
    #         breadcrumb.append(k.slug)
    #         k = k.parent
    #     for i in range(len(breadcrumb)-1):
    #         breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
    #     return breadcrumb[-1:0:-1]
