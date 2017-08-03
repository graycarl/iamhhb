from django.db import models


class PGFile(models.Model):
    name = models.CharField(
        max_length=256, unique=True, verbose_name='Full file name',
    )
    # basename = models.CharField(
    #     max_length=128, verbose_name='Base file name',
    # )
    # dirname = models.CharField(
    #     max_length=128, verbose_name='The directory path',
    #     db_index=True, blank=True
    # )
    oid = models.PositiveIntegerField(
        verbose_name='PostgreSQL LargeObject OID'
    )
    size = models.PositiveIntegerField(verbose_name='File size in bytes.')
    created_at = models.DateTimeField(auto_now_add=True)

    # def clean(self):
    #     self.dirname = os.path.dirname(self.name)
    #     self.basename = os.path.basename(self.name)

    class Meta:
        required_db_vendor = 'postgresql'
        verbose_name = 'pgfile'
