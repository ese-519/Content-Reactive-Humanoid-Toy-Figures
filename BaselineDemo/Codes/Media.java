import java.awt.Desktop;
import java.io.*;

public class Media {

	static long start ;
	static FileWriter fw;
	static BufferedWriter bw ;
	
	public static void main(String[] args) throws IOException {
		File file = new File("/home/sarath/filename.txt");

		if(file.exists())
			file.delete();
		file.createNewFile();
		fw = new FileWriter(file.getAbsoluteFile());
		bw = new BufferedWriter(fw);
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		
		Desktop.getDesktop().open(new File("/home/sarath/video1.mp4"));
		
		
		
		long prev = 0;// = System.currentTimeMillis( );
		
		
		
		
		while(true)
		{
			
			String x= br.readLine();
			if(x.equalsIgnoreCase("start"))
			{
				start = System.currentTimeMillis( );
				prev = System.currentTimeMillis( );
			}
			if(x.equalsIgnoreCase("exit"))
					break;
			long current=System.currentTimeMillis();
			printNow(x, current-prev);
			prev=current;
			
		}
		bw.close();


	}
	
	public static void printNow(String code, long timeDelayFromPrevious) throws IOException
	{
		String show=String.valueOf(System.currentTimeMillis( )-start)+":"+String.valueOf(timeDelayFromPrevious)+":";
		int flag=0;
		switch (code)
		{
		case "q" : show=show+"RHandUP"; break;
		case "a" : show=show+"RHandMID";break;
		case "z" : show=show+"RHandDOWN";break;
		case "w" : show=show+"LHandUP";break;
		case "s" : show=show+"LHandMID";break;
		case "x" : show=show+"LHandDOWN";break;
		default: flag=1;break;
		}
		//System.out.println(show);
		if(flag==0)bw.write(show+"\n");
	}

}
