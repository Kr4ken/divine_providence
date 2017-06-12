export class Task {
	key : String;
	list_key : String;
	// task_type = 
	// urgency = models.ForeignKey(Urgency)
	name : String; 
	description : String;
	special : String;
	// type : String;
	due_date:Date;
	checklist:String;
	labels:String;
	sub_task:String;
	atribute:String;
	difficult:String;
}
