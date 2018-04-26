#	-*-	coding:	utf-8	-*-
from odoo import models, fields
class myconf(models.Model):
    _name='mytodolist.myconf'
    _description='a model for a todo'
    taskname=fields.Char('Nombre de la tarea' , Required=True)
    address=fields.Boolean('Terminada', Required=True)
    startdate=fields.Date('Fecha inicio', Required=True)
    enddate=fields.Date('Fecha fin', Required=True)    
    description=fields.Char('Descripcion', Required=True)
