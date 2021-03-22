// Nivelir_4.h : main header file for the NIVELIR_4 application
//

#if !defined(AFX_NIVELIR_4_H__046D6CE2_EB3B_4401_B1A6_1045CA1AFAE2__INCLUDED_)
#define AFX_NIVELIR_4_H__046D6CE2_EB3B_4401_B1A6_1045CA1AFAE2__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"		// main symbols

/////////////////////////////////////////////////////////////////////////////
// CNivelir_4App:
// See Nivelir_4.cpp for the implementation of this class
//

class CNivelir_4App : public CWinApp
{
public:
	CNivelir_4App();

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CNivelir_4App)
	public:
	virtual BOOL InitInstance();
	//}}AFX_VIRTUAL

// Implementation

	//{{AFX_MSG(CNivelir_4App)
		// NOTE - the ClassWizard will add and remove member functions here.
		//    DO NOT EDIT what you see in these blocks of generated code !
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};


/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_NIVELIR_4_H__046D6CE2_EB3B_4401_B1A6_1045CA1AFAE2__INCLUDED_)
